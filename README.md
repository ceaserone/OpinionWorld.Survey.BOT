Usage:

Why even do it:
  ```bash
   python survey_bot.py https://opinionworldsite.com
   ```
   Or use cookie file duh:
   ```bash
   python survey_bot.py https://optionworldsite.something --cookies path/to/cookie.txt
   ```


# OpinionWorld.Survey.BOT
It's a bot Napoleon, for surveys..on Opinionworld..

![1000445490](https://github.com/user-attachments/assets/0463c12c-0bf3-4927-a7eb-2b8a0b4f5c80)
opinionworld..com

Signup
opinionworld..com/signup
(No affiliate bs here)

#Opinionworld is still one of the FAST giftcard issuers, on the net, for doing surveys...

#Trying to get this to work perfectly, that way we can make an android app for it...but this must work flawlessly first.

#Few of the features so far:<br>
Free gift cards yes please!<br>
✅ Uses your tasty cookies.txt<br>
   (Grab from valid session)<br>
✅ Opens the survey site<br>
✅ Finds and navigates to a dynamic survey link (without relying on the changing part of the URL, which updates by survey, even refreshing the survey/website)<br>
✅ Waits for the page to load properly<br>
✅ Selects radio buttoms, checkboxes, and text inputs<br>
✅ Clicks the submit button (if present)<br>
✅ Uses WebDriverWait to handle loading times smoothly<br>
✅ Closes the browaer properly after finishing<br><br>

#Make these changes to help, will be automated soon but for now...

(change css selectors)
#old:
button.submit-btn {
    color: blue;

#new:
button.new-submit-btn {
    color: blue;

#I think maybe the best:
(by class name, can be broader)
submit_button = driver.find_element(By.CLASS_NAME, "submit-bt[code]

UPDATE!!02.25.25
Update coming soon, seems they did something and im to lazy to find out
but will soon...maybe someone else will before me??

#So thats that for now....
