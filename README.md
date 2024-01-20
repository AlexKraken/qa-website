# QA Website
[![QA Website Screen Shot][website-screenshot]](https://github.com/AlexKraken/qa-website)
This is a rough draft of a Flask website that provides barcode logging and weight calculations.
Demo (hosted for free on render.com and takes a few minutes to spin up) located here: [https://qa-website.sevenwattdinosaur.com/](https://qa-website.sevenwattdinosaur.com/).

## Barcode Logger

Note that the 'Check Barcode' and 'Add Barcode' sections are actually implemented as two seperate forms. This means that the user can hit 'Enter' after scanning/typing in an input box and it will be equivalent to clicking the respective button. And regardless of which form is submitted, the focus is always returned to the first input box, with its contents selected - this allows repeated scanning to be faster as the user can scan a barcode, hit 'Enter' to check if it's in the log, and immediately scan the next barcode.


## Weight Checker


## Roadmap


- [ ] Add ability to download barcode log as a .cvs file
- [ ] Add color highlighting to messages
- [ ] Add alternating colors to barcode log
- [ ] Add ability to populate 'Barcode Logger' with info from 'Weight Checker'

[website-screenshot]: images/screenshot.png
