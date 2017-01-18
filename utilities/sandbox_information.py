import sys
from cloudshell.api.cloudshell_api import CloudShellAPISession
# from context import USER, HOST, PASSWORD


def main(args):
    if len(args) != 4: raise Exception('Check your arguments, something is wrong')
    host = args[1]
    user = args[2]
    pwd = args[3]
    # sandbox_id = args[4]
    api = CloudShellAPISession(host, username=user, password=pwd, domain='Global')
    sandbox_id = api.GetCurrentReservations().Reservations[0].Id
    sandbox = api.GetReservationDetails(sandbox_id).ReservationDescription
    webserver_params = (resource.VmDetails.VmCustomParams for resource in sandbox.Resources if 'webserv' in resource.Name).next()
    public_ip = (param.Value for param in webserver_params if param.Name == 'public_ip').next()
    return 'http://{0}:81/'.format(public_ip)

if __name__ == '__main__':
    main(sys.argv)
    # args = ['whatever' ,HOST, USER, PASSWORD, 'ee3821cc-2c68-4d78-b1aa-dbd5e945a7c6']
