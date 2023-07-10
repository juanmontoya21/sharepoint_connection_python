from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File


URL = 'https://mundialservicios.sharepoint.com/sites/ADCBarbosa738-UNIDAD2000/Documentos%20compartidos/Forms/AllItems.aspx'
Username = 'p.manufactura06@andercol.com.co'
Password = 'Akzo1818*'
relative_url  = 'D:\\Users\\p.manufactura06\\OneDrive - Centro de Servicios Mundial SAS\\Escritorio'

ctx_auth = AuthenticationContext(URL)
if ctx_auth.acquire_token_for_user(Username, Password):
  ctx = ClientContext(URL, ctx_auth)
  web = ctx.web
  ctx.load(web)
  ctx.execute_query()
  
  print(web)

filename = 'base datos.xlsx'
with open(filename, 'wb') as output_file:
    response = File.open_binary(ctx, relative_url)
    output_file.write(response.content)
    



  
