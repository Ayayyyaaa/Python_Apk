import flet as ft

comptes = []

def main(page: ft.Page):
    page.title = "T'appMotiv"
    page.window.width = 390
    page.window.height = 750
    def au_clic_image(e):
            texte_saisi = champ_saisie.value 
            message_resultat.value = f"Bienvenue {texte_saisi} !"
            page.go("/secret")
            page.update()

    image_btn = ft.Image(
        src="btn1.png", 
        width=200, 
        height=60, 
        fit="contain"
    )

    def au_survol(e):
            # e.data vaut "true" quand la souris entre, "false" quand elle sort
            if e.data:
                image_btn.src = "btn2.png"
            else:
                image_btn.src = "btn1.png"
            
            # On n'oublie pas de mettre à jour la page pour voir le changement
            page.update()

    btn_image = ft.Container(
        content=image_btn,
        on_click=au_clic_image,
        on_hover=au_survol, # C'est ici qu'on branche notre effet !
        ink=True,
    )

    champ_saisie = ft.TextField(label="Saisissez votre pseudo", hint_text="Tapez ici...")
    message_resultat = ft.Text(size=20, color="blue")

    
    

    btn_image.on_click = au_clic_image

    

    # ---------------------------------------------------
    # 2. GESTION DES ÉCRANS (ROUTAGE)
    # ---------------------------------------------------
    
    def route_change(e):
        page.views.clear()
        
        # --- ÉCRAN 1 : Accueil ---
        page.views.append(
            ft.View(
                route="/", # LA CORRECTION EST ICI (ajout de route=)
                controls=[
                    ft.Column(
                        [ft.Text("T'appMotiv", size=36, color="Cyan", weight="bold"), champ_saisie, btn_image],
                        alignment="center",
                        horizontal_alignment="center",
                        spacing=40
                    )
                ],
                vertical_alignment="center",
                horizontal_alignment="center"
            )
        )
        
        # --- ÉCRAN 2 : Le Secret ---
        if page.route == "/secret":
            page.views.append(
                ft.View(
                    route="/secret", # ET LA CORRECTION EST ICI AUSSI
                    controls=[
                        ft.Column(
                            [
                                message_resultat,
                                ft.Image(src="personnage.gif", width=250, height=250), 
                                ft.ElevatedButton("Retour à l'accueil", on_click=lambda e: page.go("/"))
                            ],
                            alignment="center",
                            horizontal_alignment="center",
                        )
                    ],
                    bgcolor="#263238",
                    vertical_alignment="center",
                    horizontal_alignment="center"
                )
            )
        
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # L'astuce pour forcer le dessin de l'écran au démarrage
    route_change(None)

ft.app(main)