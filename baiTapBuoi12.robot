*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://the-internet.herokuapp.com/login
${username}   tomsmith
${password}   SuperSecretPassword!

*** Test Cases ***
Login thành công
    Open Browser    ${URL}    Chrome
    Title Should Be    The Internet
    Input Text    id:username    ${username}
    Input Text    id:password    ${password}
    Click Button    css:button.radius
    Page Should Contain    You logged into a secure area!
    [Teardown]    Close Browser

Login thất bại - Username sai
    Open Browser    ${URL}    Chrome
    Title Should Be    The Internet
    Input Text    id:username    minhhien
    Input Text    id:password    ${password}
    Click Button    css:button.radius
    Page Should Contain    Your username is invalid!
    [Teardown]    Close Browser  

Login thất bại - Password sai
    Open Browser    ${URL}    Chrome
    Title Should Be    The Internet
    Input Text    id:username    ${username}
    Input Text    id:password    salamander
    Click Button    css:button.radius
    Page Should Contain    Your password is invalid!
    [Teardown]    Close Browser
