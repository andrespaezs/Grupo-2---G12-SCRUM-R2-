const formElement = document.getElementById("Reporte");

formElement.addEventListener("submit", (event) =>{
    event.preventDefault();
    let TipoReporte = document.getElementById("TipoReporte").value;
    let DescripcionReporte = document.getElementById("DescripcionReporte").value;
    let FechaEvento = document.getElementById("FechaEvento").value;
    let HoraEvento = document.getElementById("HoraEvento").value;
    let LugarEvento = document.getElementById("LugarEvento").value;
    let ImagenEvento = document.getElementById("archivo").value;
    let DataEvent = {
        TipoReporte : TipoReporte,
        DescripcionReporte : DescripcionReporte,
        FechaEvento : FechaEvento,
        HoraEvento : HoraEvento,
        LugarEvento : LugarEvento,
        ImagenEvento : ImagenEvento,
    }
    let DataEventJson = JSON.stringify(DataEvent);
    fetch('http://localhost:3000/Reporte', {
        method : 'POST',
        body : DataEventJson
    })
    console.log(DataEventJson);
})


