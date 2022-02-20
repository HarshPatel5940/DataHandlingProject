from DBScript import SetupUser

SetupUser()


from DHP.sudo.admin import add_admin, remove_admin

add_admin("5940")
remove_admin("5940")
