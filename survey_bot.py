#/////synacknetwork.com

import sys
import os
import random
import logging
import requests
from bs4 import BeautifulSoup

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_cookies(cookie_file):
    """Load cookies from a cookie.txt file."""
    if not os.path.exists(cookie_file):
        logging.error(f"Cookie file '{cookie_file}' not found.")
        return None

    cookies = {}
    with open(cookie_file, 'r') as file:
        for line in file:
            if not line.startswith('#') and line.strip():
                parts = line.strip().split('\t')
                if len(parts) >= 7:
                    cookies[parts[5]] = parts[6]
    return cookies

def fetch_survey(url, cookies):
    """Fetch the survey page using the provided cookies."""
    try:
        response = requests.get(url, cookies=cookies)
        if response.status_code == 200:
            return response.text
        else:
            logging.error(f"Failed to fetch survey: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        logging.error(f"Network error: {e}")
        return None

def parse_survey(html):
    """Parse the survey HTML and extract questions."""
    soup = BeautifulSoup(html, 'html.parser')
    questions = []

    # Find all input fields, textareas, and select elements
    for element in soup.find_all(['input', 'textarea', 'select']):
        question = {
            'name': element.get('name'),
            'id': element.get('id'),
            'type': element.get('type'),
            'label': None,
            'options': []
        }

        # Find the label associated with the question
        if element.get('id'):
            label = soup.find('label', {'for': element.get('id')})
            if label:
                question['label'] = label.text.strip()

        # Extract options for radio buttons, checkboxes, and dropdowns
        if element.name == 'select':
            for option in element.find_all('option'):
                question['options'].append(option.text.strip())
        elif element.get('type') in ['radio', 'checkbox']:
            parent = element.find_parent(['div', 'li', 'fieldset'])
            if parent:
                question['options'] = [opt.text.strip() for opt in parent.find_all('label')]

        questions.append(question)

    return questions

def answer_question(question):
    """Answer a survey question based on its type."""
    if question['type'] in ['text', 'textarea']:
        # Provide a predefined answer for text inputs
        return "This is a sample answer."
    elif question['type'] in ['radio', 'checkbox']:
        # Randomly select an option for multiple-choice questions
        if question['options']:
            return random.choice(question['options'])
    elif question.get('options'):
        # Handle dropdowns
        return random.choice(question['options'])
    return None

def submit_survey(url, cookies, answers):
    """Submit the survey with the provided answers."""
    try:
        response = requests.post(url, cookies=cookies, data=answers)
        if response.status_code == 200:
            logging.info("Survey submitted successfully!")
        else:
            logging.error(f"Failed to submit survey: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Network error during submission: {e}")

def answer_survey(url, cookies):
    """Answer the survey questions."""
    html = fetch_survey(url, cookies)
    if not html:
        return

    questions = parse_survey(html)
    if not questions:
        logging.warning("No questions found on the survey page.")
        return

    logging.info(f"Found {len(questions)} questions.")
    answers = {}
    for question in questions:
        answer = answer_question(question)
        if answer:
            logging.info(f"Answering question '{question.get('label', question['name'])}' with: {answer}")
            answers[question['name']] = answer

    submit_survey(url, cookies, answers)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python survey_bot.py <survey_url> [--cookies <cookie_file>]")
        sys.exit(1)

    survey_url = sys.argv[1]
    cookie_file = "cookie.txt"

    # Parse optional arguments
    if '--cookies' in sys.argv:
        cookie_file = sys.argv[sys.argv.index('--cookies') + 1]

    # Load cookies
    cookies = load_cookies(cookie_file)
    if not cookies:
        logging.error("No cookies loaded. Ensure cookie.txt is in the correct format.")
        sys.exit(1)

    # Answer the survey
    answer_survey(survey_url, cookies)