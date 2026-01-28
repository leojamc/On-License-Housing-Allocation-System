#CODE BY LEO MCCAFFERTY W24046037
#rhu.py
class RHU:
    """
    Class for handling information related to RHU's (Rehabilitating Housing Units)

    Attributes:
        cost_per_bed (float): Cost per bed of housing RHU's e.g "45.60"
        capacity (int): Number of beds in total e.g "500"
        overflow (int): Number of emergency capacity/overflow beds e.g "25"
        location (RHULocation class): Co-ordinate location of the RHU
        short_term_beds (int): Number of shirt-term beds in the RHU e.g "100"
        address (str): Address in the format Building num/City/Postcode e.g "23 Cavendish Road/Newcastle upon Tyne/ NE2 1TZ"
        phone (str): Phone number for the RHU in the format +00PHONENUMBER e.g +4402994325092
        email (str): Email address for the RHU e.g rhu@rhu.com
        contact (str): Person to contact in regards to the RHU e.g "Leo McCafferty"
        management (str): Management in charge of the RHU with email in the form NAME/EMAIL e.g "MGMT/mgmg@mgmg.com
        licensee_list (list): List of licensee ID's for licensee's currently staying in the RHU e.g ["RHF56", "RHDH56" ...]
        notes (list): List of notes related to the RHU
    """