*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  newuser
    Set Password  ValidPass123
    Set Password Confirmation  ValidPass123
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ab
    Set Password  ValidPass123
    Set Password Confirmation  ValidPass123
    Click Button  Register
    Register Should Fail With Message  Username must be at least 3 characters long.

Register With Valid Username And Too Short Password
    Set Username  validuser
    Set Password  ab
    Set Password Confirmation  ab
    Click Button  Register
    Register Should Fail With Message  Password must be at least 8 characters long.

Register With Valid Username And Invalid Password
    Set Username  validuser
    Set Password  password
    Set Password Confirmation  password
    Click Button  Register
    Register Should Fail With Message  Password must contain at least one number.

Register With Nonmatching Password And Password Confirmation
    Set Username  validuser
    Set Password  ValidPass123
    Set Password Confirmation  DifferentPass123
    Click Button  Register
    Register Should Fail With Message  Passwords do not match.

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  ValidPass123
    Set Password Confirmation  ValidPass123
    Click Button  Register
    Register Should Fail With Message  Username is already taken.

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Register Should Succeed
   Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  password123
    Go To Register Page