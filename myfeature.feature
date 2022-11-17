Feature:ChangeNameFeature
  Scenario Outline: Admin is able to edit profile
   Given Chrome Browser is launched and the URL for Metabase
   Given The URL http: // localhost: 3000 / is in Use
   And I shall be Logged in as Admin User
   When I click on settings button
   Then settings open
   When I click on account settings button
   Then account settings open
   When I click on profile button
   Then profile settings open
    When I enter new first name "<firstname>"
   Then update "<update>" button is enabled
    And I enter new last name "<lastname>"
   Then update "<update>" button is enabled
    And I enter new email "<email>"
   Then update "<update>" button is enabled
    And I set language "<language>"
   Then update "<update>" button is enabled
   When I press update  button
    Then profile is updated

    Examples:
      | firstname       | lastname      | email                     |   language  |  update  |
      | Abdur           |rafay          | l201391@lhr.nu.edu,pk     |    default  |   yes    |
      | muhammad        | rafay         | l201391@lhr.nu.edu,pk    |    default  |   yes    |
      | Abdur           | muhammad      | l201391@lhr.nu.edu,pk     |    default  |   yes    |
      | Abdur           | rafay         | l201392@lhr.nu.edu,pk     |    default  |   yes    |
      | Abdur           | rafay         | l201391@lhr.nu.edu,pk     |    chinese  |   yes    |
      | " "             | " "           | " "                       |    default  |   no     |