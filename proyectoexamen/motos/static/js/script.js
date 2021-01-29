function valida_envia() {
    //valido el nombre
    if (document.fvalida.nombre.value.length <= 2) {
        alert("El nombre tiene que ser mayor a 3 caracteres")
        document.fvalida.nombre.focus()
        return false;
    }

    if (document.fvalida.A_paterno.value.length <= 2) {
        alert("El APELLIDO tiene que ser mayor a 3 caracteres")
        document.fvalida.A_paterno.focus()
        return false;
    }

    if (document.fvalida.A_materno.value.length <= 2) {
        alert("El AMETERNO tiene que ser mayor a 3 caracteres")
        document.fvalida.A_materno.focus()
        return false;
    }
    
    
    if (document.fvalida.Telefono.value.length <= 7 ) {
        alert("El tel tiene que ser igual a 9 caracteres")
        document.fvalida.Telefono.focus()
        return false;
    } 
    

    if (document.fvalida.Comentario.value.length <= 4) {
        alert("El comentario tiene que ser mayor a 5 caracteres")
        document.fvalida.Comentario.focus()
        return false;
    }


    

    
    //el formulario se envia
    //alert("Muchas gracias por enviar el formulario");
    document.fvalida.submit();

}

