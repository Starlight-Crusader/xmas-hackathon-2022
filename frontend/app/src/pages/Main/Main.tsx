import './Main.css'
import {Col, Row, Space} from 'antd'

export function Main() {
    return (
        <div className = "Main">
            <Row> 
                <Col span = {16} ><div className = "OutWin" ></div></Col>
                <Col span={2}></Col>
                <Col span = {6} ><div className = "FotoPlace"></div></Col>
            </Row>
            <Row>
                <Col span={16}>
                    <form>
                        <input className = "FormInput" placeholder = "Enter your commands..."/>
                    </form>
                </Col>
                
            </Row>
        </div>
    )
}