import './Main.css'
import {Col, Row} from 'antd'
import { Grid } from '@material-ui/core'

export function Main() {
    return (
        <div className = "Main">
            <Row> 
                <Col span = {16}><div className = "OutWin" ></div></Col>
                <Col span = {2}></Col>
                <Col span = {6}><div className = "FotoPalce"></div></Col>
            </Row>
            {/* <Row>
                <form>
                    <input className = "FormInput" placeholder = "Enter your commands..."/>
                </form>
            </Row> */}
        </div>
    )
}