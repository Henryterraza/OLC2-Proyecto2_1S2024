import React, { useState } from "react";
import { Col, Container, Row } from 'react-bootstrap';
import Editor from '../components/Editor';
import Consola from '../components/Consola';
import Button from 'react-bootstrap/Button';
import DropdownButton from 'react-bootstrap/DropdownButton';
import Dropdown from 'react-bootstrap/Dropdown';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import fileDownload from 'js-file-download';

import axios from 'axios'


function Home() {
    const [editor, setEditor] = useState("");
    const [consola, setConsola] = useState("");
    const [errores, seterrores] = useState("");
    // const [AST, setast] = useState("");
    const [TablaSimb, setTabSimp] = useState("");
    // const [tablatokens, setTabTokens] = useState("");
    

    const interpretar = async () => {
        console.log("ejecutando")
        try {
            setConsola("ejecutando...");
            if (editor == "") {
                setConsola("No hay codigo para interpretar");
                console.log("No hay codigo para interpretar");
            } else {
                console.log(editor)
                const response = await axios.post('http://localhost:5000/interpreter', { code: editor });
                console.log(response.data);
                const { consola, errores, TablaSimb  } = response.data;
                console.log(consola);
                setConsola(consola);
                seterrores(errores);
                setTabSimp(TablaSimb);
            }
        } catch (error) {
            console.log(error);
            setConsola("Error en el servidor");
        }
    };


    const ReporteErrores = async () => {
        let text = `<!doctype html>
        <html lang="en">
        <head>
             <meta charset="utf-8">
             <meta name="viewport" content="width=device-width, initial-scale=1">
             <title>Tabla Errores</title>
             <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css " rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
        </head>
        <body style="background-color: #f0efe9;">      <div class="text-center mb-5">
                 <h1 class="display-4 text-black">REPORTE DE ERRORES</h1>    
             </div>
             <div class="container">
                 <div class="row">
                     <div class="col">
                         <table class="table">
                             <thead>
                                 <tr>
                                     <th scope="col">No.</th>
                                     <th scope="col">Descripcion</th>
                                     <th scope="col">Ambito</th>
                                     <th scope="col">Linea</th>
                                     <th scope="col">Columna</th>
                                     <th scope="col">Tipo</th>
                                 </tr>
                             </thead>
                             <tbody class="table-group-divider"> `

                             text += errores;

                            
        text += `</tbody>
        </table>
    </div>
</div>
</div>


<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js"
integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2"
crossorigin="anonymous"></script>
</body>

</html>`

        fileDownload(text, "Reporte_Errores.html");

    }



      


    const ReporteSimbolos = async () => {
        let text = `<!doctype html>
        <html lang="en">
        <head>
             <meta charset="utf-8">
             <meta name="viewport" content="width=device-width, initial-scale=1">
             <title>Tabla Simbolos</title>
             <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css " rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
        </head>
        <body style="background-color: #f0efe9;">      <div class="text-center mb-5">
                 <h1 class="display-4 text-black">REPORTE DE ERRORES</h1>    
             </div>
             <div class="container">
                 <div class="row">
                     <div class="col">
                         <table class="table">
                             <thead>
                                 <tr>
                                     <th scope="col">Identificador</th>
                                     <th scope="col">Tipo simbolo</th>
                                     <th scope="col">Tipo dato</th>
                                     <th scope="col">Ambito</th>
                                     <th scope="col">Linea</th>
                                     <th scope="col">Columna</th>
                                 </tr>
                             </thead>
                             <tbody class="table-group-divider"> `

                             text += TablaSimb;

                            
        text += `</tbody>
        </table>
    </div>
</div>
</div>


<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js"
integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2"
crossorigin="anonymous"></script>
</body>

</html>`

        fileDownload(text, "Reporte_Simbolos.html");

    }

    // const ReporteDot = () => {
    //     window.open('https://quickchart.io/graphviz?graph=%20'+ AST, '_blank');
    //     fileDownload(AST, "ast.dot");
        
    //   }

    return (
        <Container>
            <Row>
                <Col style={{ textAlign: 'left' }}>
                    <Editor input={setEditor} />
                </Col>


                <Col>
                <Col>
                    <Button variant="outline-success" onClick={() => interpretar()} >Run</Button>{' '}
                </Col>
                <Col>
                    <h1>-----------</h1>
                </Col>
                
                <Col>
                    <DropdownButton as={ButtonGroup} title="Dropdown" id="bg-nested-dropdown">
                        <Dropdown.Item onClick={() => ReporteErrores()} eventKey="1">Reporte Errores</Dropdown.Item>
                        <Dropdown.Item onClick={() => ReporteSimbolos()} eventKey="2">Reporte Tabla Simbolos</Dropdown.Item>
                    </DropdownButton>

                </Col>
                </Col>
            </Row>
            <Row>
                <Col style={{ textAlign: 'left' }}>
                    <h3>Consola</h3>
                </Col>

            </Row>
            <Row>
                <Col style={{ textAlign: 'left' }}>
                    <Consola consola={consola} />
                </Col>

            </Row>

            {/* seccion de botones */}
           


        </Container>
    );

}

export default Home;