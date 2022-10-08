const express = require('express');
const cors = require('cors')


const app = express()
const port = 3000

let ReportData = []

app.use(
    express.urlencoded({
        extended : true
    })
)


app.use(express.json({ 
    type : "*/*"
}))


app.use(cors());

app.get('/Reportes', (req, res) => {
    res.send(JSON.stringify(ReportData))
})

app.post('/Reporte', (req, res) =>{
    let Reporte = req.body
    ReportData.push(Reporte)
    res.send(JSON.stringify("Reporte Recibido"))
    console.log(ReportData)
})
app.listen(port, () => {
    console.log('Estoy ejecutando en http://localhost:3000')
})