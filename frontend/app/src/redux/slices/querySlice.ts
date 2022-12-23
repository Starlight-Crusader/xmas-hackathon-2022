import { createAsyncThunk, createSlice, PayloadAction } from "@reduxjs/toolkit";
import axios from 'axios';
const api = `http://127.0.0.1:8000/api/`;

// action
export const sendQuery = createAsyncThunk(
 'query/send',
 async(q : string) => {
    console.log(q);
        return await axios.post(api +`parser/`).then((res) => {
            console.log(res.data);
            return res.data;
        })
 }
)