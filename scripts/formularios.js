// Envío de los formularios del sitio al correo de Anik con Web3Forms (https://web3forms.com).
// La clave de acceso se obtiene en web3forms.com con el correo que recibirá los mensajes.
// Es pública por diseño: solo sirve para enviar formularios a ese correo.
const WEB3FORMS_CLAVE = '64979929-c831-4214-8175-ae1f3394726f';

// Cada campo viaja con su atributo name, que es el rótulo que aparece en el correo.
// El campo "email" queda como dirección de respuesta. La nota .form-note del formulario
// trae el mensaje de éxito y se reutiliza para los estados de envío y de error.
const conectarFormulario = (form, asunto, alExito) => {
  const boton = form.querySelector('[type="submit"]');
  const nota = form.querySelector('.form-note');
  const exito = nota.innerHTML;
  const avisar = (html, esError = false) => {
    nota.innerHTML = html;
    nota.classList.toggle('is-error', esError);
    nota.hidden = false;
  };

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    boton.disabled = true;
    avisar('Enviando…');
    try {
      if (!WEB3FORMS_CLAVE) throw new Error('Falta la clave de acceso de Web3Forms en scripts/formularios.js');
      const datos = new FormData(form);
      datos.append('access_key', WEB3FORMS_CLAVE);
      datos.append('subject', typeof asunto === 'function' ? asunto() : asunto);
      datos.append('from_name', 'anikjimenez.com');
      const respuesta = await fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        headers: { Accept: 'application/json' },
        body: datos,
      });
      const resultado = await respuesta.json();
      if (!respuesta.ok || !resultado.success) throw new Error(resultado.message || respuesta.status);
      form.reset();
      avisar(exito);
      if (typeof alExito === 'function') alExito();
    } catch (error) {
      console.error('No se pudo enviar el formulario:', error);
      avisar('No se pudo enviar el formulario. Inténtalo de nuevo o escríbeme a <a href="mailto:escritora@anikjimenez.com">escritora@anikjimenez.com</a>.', true);
    } finally {
      boton.disabled = false;
    }
  });
};
