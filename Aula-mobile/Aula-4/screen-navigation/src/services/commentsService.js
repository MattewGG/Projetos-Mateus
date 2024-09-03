import axios from "axios"

const URL = 'https://66d633acf5859a7042689e6b.mockapi.io/api/v1/comments'



// toda funcao coema com feth seguido por alguma coisa ex fetchCommentById

export const fetchComments = async () => {
    const response = await axios.get(URL)

    return response.data
}

export const fetchCommentById = async (id) => {
    const response = await axios.get(`${URL}/${id}`)

    return response.data
}




