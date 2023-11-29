function exibir_form(tipo){

    add_mecanico = document.getElementById('adicionar-mecanico')
    att_mecanico = document.getElementById('att_mecanico')
    btnAttMecanico = document.getElementById('btn-att-mecanico')
    btnAddMecanico = document.getElementById('btn-add-mecanico')
  
    if(tipo == "1"){
        att_mecanico.style.display = "none"
        add_mecanico.style.display = "block"
        btnAddMecanico.style.display = "none"
        btnAttMecanico.style.display = "block"

    }else if(tipo == "2"){
        add_mecanico.style.display = "none";
        att_mecanico.style.display = "block"
        btnAddMecanico.style.display = "block"
        btnAttMecanico.style.display = "none"
    }

}


function dados_mecanico(){
    mecanico = document.getElementById('mecanico-select')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    id_mecanico = mecanico.value

    data = new FormData()
    data.append('id_mecanico', id_mecanico)

    fetch("/mecanicos/atualiza_mecanico/",{
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data

    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('form-att-mecanico').style.display = 'block'
        
        id = document.getElementById('id')
        id.value = data['mecanico_id']

        nome = document.getElementById('nome')
        nome.value = data['mecanico']['nome']

        sobrenome = document.getElementById('sobrenome')
        sobrenome.value = data['mecanico']['sobrenome']

        cpf = document.getElementById('cpf')
        cpf.value = data['mecanico']['cpf']

        email = document.getElementById('email')
        email.value = data['mecanico']['email']
    })


}


function update_mecanico(){
    nome = document.getElementById('nome').value
    sobrenome = document.getElementById('sobrenome').value
    email = document.getElementById('email').value
    cpf = document.getElementById('cpf').value
    id = document.getElementById('id').value

    fetch('/mecanicos/update_mecanico/' + id, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify({
            nome: nome,
            sobrenome: sobrenome,
            email: email,
            cpf: cpf,
        })

    }).then(function(result){
        return result.json()
    }).then(function(data){

        if(data['status'] == '200'){
            nome = data['nome']
            sobrenome = data['sobrenome']
            email = data['email']
            cpf = data['cpf']
            console.log('Dados alterado com sucesso')
        }else{
            console.log('Ocorreu algum erro')
        }

    })

}
