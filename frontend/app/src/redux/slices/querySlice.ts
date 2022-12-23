import { createAsyncThunk, createSlice, PayloadAction, SerializedError } from "@reduxjs/toolkit";
import axios from 'axios';
import { useAppDispatch } from "../hooks/hooks";
const api = `http://127.0.0.1:8000/`;
 
export interface QuizQuestion{
    id: number;
    question_text: string;
}

interface Meme{
    id: number;
    image_URL: string;
    topic: string;
}

interface QueryState{
    meme: Meme[] | null;
    endpoint: string ;
    loading: string;
    error: SerializedError |null;
    quiz: QuizQuestion[] | null;

}

const initialState: QueryState = {
    endpoint: '',
    loading: '',
    error: null,
    quiz: null,
    meme: null,
}
// action
export const sendQuery = createAsyncThunk(
 'query/send',
 async(command : string) => {
        console.log(command);
        return await axios.post(api +`api/parseapp/`, {command}).then((res) => {
            console.log(res.data);
            return res.data;
        })
 }
)

export const second = createAsyncThunk(
    'query/second',
    async(endpoint: string) => {
        return await axios.get(api + endpoint).then((res) => {
            console.log(res.data);
            return res.data;
        })
    }
)

export const querySlice = createSlice({
    name: 'query',
    initialState,
    reducers:{
        getQuery :(state: QueryState, action: PayloadAction<string>) =>{
            state.endpoint = action.payload;
        }
    },
   extraReducers:(builder)=>{
    builder.addCase(sendQuery.pending, (state) =>{
        state.loading = 'pending';
    }).addCase(sendQuery.fulfilled, (state, payload) =>{
        state.loading = 'fulfilled';
        state.endpoint = payload.payload;
        console.log(state.endpoint);
    }).addCase(sendQuery.rejected, (state, payload) =>{
        state.loading = 'rejected';
        state.error = payload.error;
        console.log(payload.error.message);
    }).addCase(second.pending, (state) =>{
        state.loading = 'pending';
    }).addCase(second.fulfilled, (state, payload) =>{
        state.loading = 'fulfilled';
        if(payload.payload.length > 1){
            state.quiz = payload.payload;
            console.log(payload.payload.length);
        } else if (payload.payload['image_URL'] !== null){
            state.meme = payload.payload;
        }

        
        console.log(state.endpoint);
      }).addCase(second.rejected, (state, payload) =>{
        state.loading = 'rejected';
        state.error = payload.error;
        console.log(payload.error.message);
    })
}})

export const {getQuery} = querySlice.actions;
export default querySlice.reducer;