import './Main.css'
import {Col, Input, Row} from 'antd'
import { useAppDispatch, useAppSelector } from '../../redux/hooks/hooks'
import { QuizQuestion, second, sendQuery } from '../../redux/slices/querySlice';
import { useState } from 'react';

export function Main() {
  
    const dispatch = useAppDispatch();
    const {endpoint, quiz, meme} = useAppSelector((state) => ({...state.query}))
    const [message, setMessage] = useState('');
    const [updated, setUpdated] = useState('');

    const handleChange = (event:any) => {
        setMessage(event.target.value);
      };
    
      const handleKeyDown = (event: any) => {
        if (event.key === 'Enter') {
          // 👇 Get input value
          setUpdated(message);
          console.log(message);
          dispatch(sendQuery(message));
          dispatch(second(endpoint));
          
        }
      };
    
      function Quiz(){
        return <>{quiz?.map(({question_text}: QuizQuestion) => (
          <>
            {question_text}
          </>
        ))}</>
      }
     return (
        <div className = "Main">
            <Row> 
                <Col span = {16} ><div className = "OutWin"  style ={{paddingLeft: "30px", paddingTop:"10px"}}>$ {updated}
                  {quiz !== null? <>
                  {quiz.map(({question_text}: QuizQuestion) => (
                    <> <br/>{question_text}</>
                  ))}
                  </> : <></>}
                  </div>
                </Col>
                
                <Col span={2}></Col>
                <Col span = {6} ><div>
                  {meme !== null? <img style={{width: "200px", height:"200px"}} src={meme[0].image_URL} /> : <></>}
                  {/* <img src="https://drive.google.com/uc?export=view&id=1UnS5flbGKZQ-86U3bKvV4n02Rb5ogiTz" alt="blu" /> */}
       
              </div></Col>
            </Row>
            <Row>
                <Col span={16}>
                   
                        <input className = "FormInput" placeholder = "Enter your commands..."
                        type="text"
                        id="message"
                        name="message"
                        value={message}
                        onChange={handleChange}
                        onKeyDown={handleKeyDown}/>

                </Col>
                
            </Row>
        </div>
    )
}