
import plivo

auth_id = "MAMDLKNJC1OGU5NTLJNZ"

auth_token = "ODcwMDFjZjJiZjE5MzMzMGU5MDBkM2FlMWMwOGMy"

p = plivo.RestAPI(auth_id,auth_token)

params = {
          
        'dst' : '8885558748',
        'text' : u"Sent with love from python"
        
    }

response = p.send_message(params)


print str(response)
