import React from 'react';
import CodeMirror from '@uiw/react-codemirror';
import { javascript } from '@codemirror/lang-javascript';
import { okaidia, okaidiaInit } from '@uiw/codemirror-theme-okaidia';

function Editor(props) {
  const [value, setValue] = React.useState("");
  const onChange = React.useCallback((val, viewUpdate) => {
    props.input(val)
    console.log('val:', val);
    setValue(val);
  }, []);
  return <CodeMirror value={value} height="550px" width='635px' theme={okaidia} extensions={[javascript({ jsx: true })]} onChange={onChange} />;
}
export default Editor;
