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

    def add_dialog(self, type_d:str = 'error', icon:str = None, title:str = None, text:str = None, ):
        match type_d:
            case 'error':
                self.dialog = MDDialog(
                    MDDialogIcon(
                        icon=icon if icon else 'alert',
                        theme_font_size='Custom',
                        font_size='50sp'
                    ),
                    MDDialogHeadlineText(
                        text=title if title else ''
                    ),
                    MDDialogSupportingText(
                        text=text if text else ''
                    ),
                    MDDialogButtonContainer(
                        MDWidget(),
                        MDButton(
                            MDButtonText(
                                text="ОК"
                            ),

                            on_press=lambda *args: self.dialog.dismiss()
                        )
                    )
                )

            case 'msg':
                self.dialog = MDDialog(
                    MDDialogIcon(
                        icon=icon if icon else 'information-outline',
                        theme_font_size='Custom',
                        font_size='50sp'
                    ),
                    MDDialogHeadlineText(
                        text=title if title else ''
                    ),
                    MDDialogSupportingText(
                        text=text if text else ''
                    ),
                    MDDialogButtonContainer(
                        MDWidget(),
                        MDButton(
                            MDButtonText(
                                text="ОК"
                            ),

                            on_press=lambda *args: self.dialog.dismiss()
                        )
                    )
                )

        self.dialog.open()

    def app_login(self, login, password):
        global session
        print('Кнопка нажата!')

        if login == '1' and password == '1':
            #Авторизация успешна
            session['login'] = login
            session['token'] = token_hex(16)
            self.root.current = 'main'
            self.add_dialog(type_d='msg', title='Добро пожаловать', text=f'Рады вас видеть,{login}')
        else:
            self.add_dialog(title='Ошибка', text='Неверный логин или пароль')

    def app_logout(self, login, password, rpassword):
        if login in ['a', 'log', 'admin', 'root']:
            self.add_dialog(title='Регистрация', text='Данный логин уже существует!')
            return

#       if mt('[0-9a-Za-z@_!]{8, 36}', password):
#           self.add_dialog(title='Регистрация', text='Пароль не соответствует требованиям!')
#           return

        if rpassword != password:
            self.add_dialog(title='Регистрация', text='Пароли не совпадают!')
            return


MainApp().run()
