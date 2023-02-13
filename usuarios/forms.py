from django import forms

class LoginForms(forms.Form):
    nome_login= forms.CharField(
        label= "Nome de login",
        required= True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder": "Ex: Domenica"
            }
        )
    )



    senha = forms.CharField(
        label="Senha",
        required= True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder": "Digite a senha"
            }
        )
    )


class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label= "Nome de cadastro",
        required= True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder": "Ex: Domenica"
            }
        )
    )

    email= forms.EmailField(
        label="Email pessoal",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: Domenica.priscilao@ivymail.com"}
        )
    )

    senha1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a senha"
            }
        )
    )

    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a senha novamente6"
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError('NOME DE USUÁRIO NÃO DEVE CONTER ESPAÇOS')
            else:
                return nome

    def clean_senha(self):
        senha = self.cleaned_data.get("senha")
        senha1= self.cleaned_data.get("senha1")
        if senha != senha1:
            raise forms.ValidationError("SENHAS NÃO COINCIDEM")

        else:
            return senha


