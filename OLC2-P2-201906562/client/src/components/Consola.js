import React from 'react';
import CodeMirror from '@uiw/react-codemirror';
import { okaidia, okaidiaInit } from '@uiw/codemirror-theme-okaidia';


function Consola(props) {
 
  return (
    <CodeMirror
    value={props.consola}
    theme={okaidia}
    height="250px"
    width='1035px'
  />
  );
}
export default Consola;