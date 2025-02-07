
from random import randint
from kivymd.app import MDApp
from kivy.lang import Builder
from secrets import token_hex
from datetime import date, datetime
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import MDDialogIcon, MDDialog, MDDialogHeadlineText, MDDialogSupportingText, MDDialogButtonContainer
from kivymd.uix.widget import MDWidget
from kivymd.uix.transition import MDSharedAxisTransition

class MainApp(MDApp):
    dialog = None

    def build_config(self, config):
        config.setdefaults('THEMING', {
            'theme_style': 'Light',
            'primary_palette': 'Green'
        })

        config.setdefaults('SESSION', {
            'login': None,
            'token': None,
            'last_login': None
        })
        pass

    def build(self):
        self.theme_cls.theme_style = self.config.get('THEMING', 'theme_style')
        self.theme_cls.primary_palette = self.config.get('THEMING', 'primary_palette')
        self.root = Builder.load_file("ui.kv")

        self.root.transition = MDSharedAxisTransition(
            transition_axis='x',
            duration=.5
        )

        if self.config.get('SESSION', 'token') != 'None' and self.check_session():
            self.root.current = 'main'
            return self.root

    def start_game(self):
        self.root.current = 'game'

    def add_dialog(self, type_d: str = 'error', title: str = None, text: str = None, icon: str = None):
        match type_d:
            case "error":
                self.dialog = MDDialog(
                    MDDialogIcon(
                        icon=icon if icon else 'alert',
                        theme_font_size='Custom',
                        font_size='32sp'
                    ),
                    MDDialogHeadlineText(
                        text=title if title else ''
                    ),
                    MDDialogSupportingText(
                        text=text if text else ''
                    ),
                    MDDialogButtonContainer(
                        MDWidget(),
                        MDButton(MDWidget(),
                                 MDButtonText(
                                     text="ОК"
                                 ),
                                 on_press=lambda *args: self.dialog.dismiss()
                                 )
                    )
                )
            case "msg":
                self.dialog = MDDialog(
                    MDDialogIcon(
                        icon=icon if icon else 'information-outline',
                        theme_font_size='Custom',
                        font_size='32sp'
                    ),
                    MDDialogHeadlineText(
                        text=title if title else ''
                    ),
                    MDDialogSupportingText(
                        text=text if text else ''
                    ),
                    MDDialogButtonContainer(
                        MDWidget(),
                        MDButton(MDWidget(),
                                 MDButtonText(
                                     text="ОК"
                                 ),
                                 on_press=lambda *args: self.dialog.dismiss()
                                 )
                    )
                )
        self.dialog.open()

    def radio_change_color(self, checkbox, active):
        if active:
            self.theme_cls.primary_palette = checkbox.value
            self.config.set('THEMING', 'primary_palette', checkbox.value)
            self.config.write()

    def app_login(self, login, password):
        print('Кнопка нажата!')
        if login == 'a' and password == 'a':
            self.config.set('SESSION', 'login', login)
            self.config.set('SESSION', 'token', token_hex())
            self.config.set('SESSION', 'last_login', str(datetime.now()))
            self.config.write()
            self.root.current = 'main'
            self.add_dialog(type_d='msg', title=f'Добро пожаловать,{login}', text=f'ЕСЛИ ЧО ЗАХОДИ')
        else:
            self.add_dialog(title='Авторизация!', text='Неправильный логи или пароль!')
            self.root.ids.login_login = ''
            self.root.ids.login_password = ''
            self.dialog.open()

    def close_session(self):
        self.config.set('SESSION', 'login', None)
        self.config.set('SESSION', 'password', None)
        self.config.set('SESSION', 'last_login', None)
        self.config.write()
        self.root.current = 'Login'

    def check_session(self):
        if randint(0, 2):
            self.config.set('SESSION', 'last_login', None)
            self.config.write()
            return True
        else:
            self.config.set('SESSION', 'login', None)
            self.config.set('SESSION', 'password', None)
            self.config.set('SESSION', 'last_login', None)
            self.config.write()

    def app_logout(self, login, password, rpassword):
        if login in ['a', 'b', 'c', '']:
            self.add_dialog(title='Ошибка регистрации', text='Пользователь существует или поле пустое!')
            return
        # if mt('[0-9A-Za-z@_!]{8,36}'):
        #     self.add_dialog(title='Регистрация', text='Пользователь существует!')
        #     return
        if rpassword != password:
            self.add_dialog(title='Регистрация', text='Пароль не совпадает!')
            return

        self.root.ids.register_login.text = ''
        self.root.ids.register_password.text = ''
        self.root.ids.register_rpassword.text = ''
        self.root.current = 'Login'
        self.add_dialog(type_d='msg', title='УСПЕШНО', text='Вы перенаправлены на окно авторизации.')

    def app_register(self, register, password):
        pass


MainApp().run()
