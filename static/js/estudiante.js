function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const form_create = document.querySelector('#form_create');
form_create.onsubmit = () => {
    const data = new FormData(form_create);
    const map = new Map(data.entries());
    let obj = {
        'dni': map.get('dni'),
        'nombre': map.get('nombre'),
        'apellido': map.get('apellido'),
        'estado': map.get('estado'),
    };
    // alert(obj);
    create_estudiante(obj);
    return false;
};
// FUNCION PARA CREAR DATOS DEL API REST
async function create_estudiante(data){
    let url = '/app/api/estudiante/';
    var csrftoken = getCookie('csrftoken');
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            "X-CSRFToken": csrftoken
        },
        body: JSON.stringify(data),
    })
    .then(res => res.json())
    .then(() => {
        list_estudiante();
        form_create.reset();
    });
};
// FUNCION PARA LISTAR DATOS DEL API REST
async function list_estudiante(){
    let url = '/app/api/estudiante/';
    var csrftoken = getCookie('csrftoken');
    const response = await fetch(url, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            "X-CSRFToken": csrftoken
        }
    })
    .then(res => res.json())
    .then((res) => {
        let table = document.getElementById("tabla_estudiante").getElementsByTagName("tbody")[0];
        table.innerHTML = "";
        for(let i = 0; i < res.length; i++){
            // console.log(res[i])
            let estado = "";
            if (res[i].estado === '0'){
                estado = "<span class='badge badge-danger'>Deshabilitado</span>"
            }
            else{
                estado = "<span class='badge badge-success'>Habilitado</span>"
            }
            table.insertRow().innerHTML = "<tr><td>"+res[i].dni+"</td><td>"+res[i].nombre+"</td><td>"+res[i].apellido+"</td><td>"+estado+"</td><td><button class='btn btn-warning btn-xs' onclick='openmodal_estudiante("+JSON.stringify(res[i])+");'><i class='fa fa-edit'></i></button> <button class='btn btn-danger btn-xs' onclick='delete_estudiante("+res[i].id+");'><i class='fa fa-trash'></i></button></td></tr>";
        }
    });
};
list_estudiante();
// FUNCION PARA ELIMINAR DATOS DEL API REST
async function delete_estudiante(id){
    if(confirm("¿Desea eliminar el registro?")){
        let url = '/app/api/estudiante/'+id;
        var csrftoken = getCookie('csrftoken');
        const response = await fetch(url, {
            method: 'DELETE',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                "X-CSRFToken": csrftoken
            },
        })
        .then(() => {
            list_estudiante();
            alert("Registro Nro." + id + " eliminado");
        });
    }
};
// FUNCION PARA ACTUALIZAR DATOS DEL API REST
function openmodal_estudiante(data){
    // console.log(data);
    document.getElementById('e_id').value = data['id'];
    document.getElementById('e_dni').value = data['dni'];
    document.getElementById('e_nombre').value = data['nombre'];
    document.getElementById('e_apellido').value = data['apellido'];
    document.getElementById('e_estado').value = data['estado'];
    $("#modaledit-estudiante").modal();
};
const form_edit = document.querySelector('#form_edit');
form_edit.onsubmit = () => {
    const data = new FormData(form_edit);
    const map = new Map(data.entries());
    let obj = {
        'dni': map.get('e_dni'),
        'nombre': map.get('e_nombre'),
        'apellido': map.get('e_apellido'),
        'estado': map.get('e_estado'),
    };
    let id = map.get('e_id');
    update_estudiante(id, obj);
    return false;
};

async function update_estudiante(id, data){
    let url = '/app/api/estudiante/'+id+'/';
    var csrftoken = getCookie('csrftoken');
    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            "X-CSRFToken": csrftoken
        },
        body: JSON.stringify(data),
    })
    .then(res => res.json())
    .then(() => {
        list_estudiante();
        form_edit.reset();
        $("#modaledit-estudiante").modal('hide');
    });
};