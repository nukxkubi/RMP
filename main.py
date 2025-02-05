from kivymd.app import MDApp
from kivy.lang import Builder
from secrets import token_hex

from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import MDDialogIcon, MDDialog, MDDialogHeadlineText, MDDialogSupportingText, MDDialogButtonContainer
from kivymd.uix.widget import MDWidget

session = {
    'login': '',
    'token':''
}

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Aqua"
        self.root = Builder.load_file("ui.kv")
        return self.root

    def radio_change_color(self, checkbox, active):
        if active:
            self.theme_cls.primary_palette  = checkbox.value

    def app_login(self, login, password):
        global session
        print('Кнопка нажата!')

        if login == '1' and password == '1':
            #авторизация успешна
            session['login'] = login
            session['token'] = token_hex(16)
            self.root.current = 'main'
            self.dialog = MDDialog(
                MDDialogIcon(
                    icon='smile',
                    theme_font_size='Custom',
                    font_size = '50sp'
                ),
                MDDialogHeadlineText(
                    text=f'Добро пожаловать'
                ),
                MDDialogSupportingText(
                    text=f'Рады вас видеть, {login}!'
                ),
                MDDialogButtonContainer(
                    MDWidget(),
                    MDButton(
                        MDButtonText(
                            text="НЕТ"
                        ),

                        on_press=lambda *args: exit()
                    ),
                    MDButton(
                        MDButtonText(
                            text ="ОК"
                        ),

                        on_press=lambda *args: self.dialog.dismiss()
                    )
                )
            )

            self.dialog.open()

        else:
            self.dialog = MDDialog(
                MDDialogIcon(
                    icon='alert',
                    theme_font_size='Custom',
                    font_size = '50sp'
                ),
                MDDialogHeadlineText(
                    text='ОШИБКА'
                ),
                MDDialogSupportingText(
                    text='Неправильный логин или пароль!'
                ),
                MDDialogButtonContainer(
                    MDWidget(),
                    MDButton(MDWidget(),
                        MDButtonText(
                            text ="ОК"
                        ),

                        on_press = lambda *args: self.dialog.dismiss()
                    )
                )
            )
            self.dialog.open()

            def app_register(self, register, password):
                pass

MainApp().run()
