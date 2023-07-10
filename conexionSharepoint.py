from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext

class Sharepoint:
    def __init__(self, site_url, username, password):
        self.site_url = site_url
        self.username = username
        self.password = password
        self.ctx = None
        self.sp_list = None

    def connect_to_list(self, list_title):
        # Crea un contexto de autenticación
        auth_ctx = AuthenticationContext(self.site_url)
        auth_ctx.acquire_token_for_user(self.username, self.password)

        # Crea un contexto de cliente para SharePoint
        self.ctx = ClientContext(self.site_url, auth_ctx)

        # Abre la lista de SharePoint
        self.sp_list = self.ctx.web.lists.get_by_title(list_title)

    def print_list_items(self):
        # Obtiene todos los elementos de la lista
        items = self.sp_list.items.get()

        # Carga los datos de los elementos
        self.ctx.load(items)
        self.ctx.execute_query()

        # Imprime los elementos
        for item in items:
            print(item.properties.values())

# Configura los detalles de autenticación y conexión a SharePoint
site_url = "https://mundialservicios.sharepoint.com/sites/ADCBarbosa738-UNIDAD2000"
username = "p.manufactura06@andercol.com.co"
password = "Akzo1818*"
list_title = "Rendimiento U2000"

# Crea una instancia de la clase Sharepoint y conecta a la lista
rendimiento = Sharepoint(site_url, username, password)
rendimiento.connect_to_list(list_title)

# Imprime los elementos de la lista
rendimiento.print_list_items()