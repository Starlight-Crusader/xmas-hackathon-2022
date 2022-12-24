import "./Main.css";
import { Col, Input, Row, Image } from "antd";
import { useAppDispatch, useAppSelector } from "../../redux/hooks/hooks";
import { QuizQuestion, second, sendQuery } from "../../redux/slices/querySlice";
import { useState } from "react";
import { useEffect } from "react";

export function Main() {
  useEffect(() => {
    sessionStorage.setItem("auth", "false");
  }, []);
  let auth = false;

  const dispatch = useAppDispatch();
  const { endpoint, quiz, meme, loading } = useAppSelector((state) => ({
    ...state.query,
  }));
  const [message, setMessage] = useState("");
  const [updated, setUpdated] = useState("");

  function delay(ms: number) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }

  const handleChange = (event: any) => {
    setMessage(event.target.value);
  };
  let i = 0;

  const handleKeyDown = async (event: React.KeyboardEvent<HTMLDivElement>) => {
    if (event.repeat) {
      console.log("repeat");
      return;
    }
    if (event.key === "Enter") {
      // 👇 Get input value
      setUpdated(message);
      setMessage("");
      let marker = false;
      // debugger;
      if (
        sessionStorage.getItem("auth") === "false" &&
        message === "vdov goodafternoon"
      ) {
        sessionStorage.setItem("auth", "true");
        return;
      }

      dispatch(sendQuery(message));
    }
  };

  if (endpoint !== "") {
    if (i <= 0) {
      dispatch(second(endpoint));
      i++;
    }
  }

  return (
    <div className="Main">
      
      <Row>
        <Col span={16}>
          <div
            className="OutWin"
            style={{ paddingLeft: "30px", paddingTop: "10px" }}
          >
            $ {updated} <br />
            {sessionStorage.getItem('auth') === "false" ? (
              <>
                good afternoon <br />
              </>
            ) : quiz !== null ? (
              <>
                {quiz.map(({ question_text }: QuizQuestion) => (
                  <>
                    {" "}
                    <br />
                    {question_text}
                  </>
                ))}
              </>
            ) : (
              <></>
            )}
          </div>
        </Col>

        <Col span={2}></Col>
        <Col span={6}>
          <div>
            {meme !== null ? (
              <Image
                style={{
                  width: "300px",
                  height: "300px",
                  borderRadius: "10px",
                  border: "2px solid white",
                }}
                src={meme[0].image_URL}
              />
            ) : (
              <div
                style={{
                  width: "300px",
                  height: "300px",
                  borderRadius: "10px",
                  border: "2px solid white",
                  backgroundColor: "black",
                }}
              ></div>
            )}
          </div>
        </Col>
      </Row>
      <Row>
        <Col span={16}>
          <input
            className="FormInput"
            placeholder="Enter your commands..."
            type="text"
            id="message"
            name="message"
            value={message}
            onChange={handleChange}
            onKeyDown={handleKeyDown}
          />
        </Col>
      </Row>
    </div>
  );
}
