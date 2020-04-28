#WLS_UserCreation.py

def file_parse():
    global _dict
    _dict={}
    usrprop = "WLSusers.properties"
    if os.path.exists(usrprop):
        fo = open(usrprop,'r+')
        lines = fo.readlines()
        for usr in lines:
            if "=" in usr:
                usr = usr.rstrip()
                key = usr.split('=')[0]
                value = usr.split('=')[1]
                _dict[key]=value
    else:
        print(usrprop+"property file is missing!")


def connect_domain():
    try:
        AdmSvr = _dict.get('hostname')
        AdmPort = _dict.get('port')
        AdmUsr = _dict.get('admin_username')
        AdmPwd = _dict.get('admin_password')
        AdmUrl = "t3://"+AdmSvr+":"+AdmPort
        print("connecting to Admin Server")
        connect(AdmUsr, AdmPwd, AdmUrl)
    except Exception, error:
        print("\n Unable to connect to admin server \n")
        print("\n please verify the url or make sure the AdminServer is up and Running:\n")
        print("Error description as follows:\n")
        print(error)
        print dumpStack()
        exit()

def creating_user():
    try:
        domainName = _dict.get('dname')
        realmName = _dict.get('rname')
        print("")
        authpath= '/SecurityConfiguration/' + domainName + '/Realms/' + realmName + '/AuthenticationProviders/DefaultAuthenticator'
        cd(authpath)
        cmo.createUser(uname,upwd,udesc)
        print(uname + " user created")
    except Exception, error:
        print("Failed to create User, Make sure that the User name is not already present")
        print("Make sure the the Password is atleast of 8 characters")
def adding_to_group():
    try:
        domainName = _dict.get('dname')
        realmName = _dict.get('rname')
        authpath= '/SecurityConfiguration/' + domainName + '/Realms/' + realmName + '/AuthenticationProviders/DefaultAuthenticator'
        cd(authpath)
        cmo.addMemberToGroup(grpname, uname)
        print("Added to group" "  -  " + grpname)
    except Exception, error:
        print("Failed to Add in group")


if __name__ != "__main__":
    import os
    import sys
    #redirect("/dev/null",'false')
    file_parse()
    connect_domain()
    users = _dict.get('wlusers').split(',')
    for each_user in users:
        uname = _dict.get(each_user+'.Name')
        upwd = _dict.get(each_user+'.passwd')
        udesc = _dict.get(each_user+'.desc')
        grpname = _dict.get(each_user+'.group')
        creating_user()
        adding_to_group()
        print"------------------------------------------------------------"


if __name__ == "__main__":
    print('Please execute the script via WLST')