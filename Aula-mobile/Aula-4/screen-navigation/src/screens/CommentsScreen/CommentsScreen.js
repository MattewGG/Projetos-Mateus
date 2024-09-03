import React from "react"
import { View } from "react-native"
import { useQuery } from "react-query"
import { fetchComments } from "../../services/commentsService"

export default function CommentsScreen () {
    const { data: comments, isLoading, isFetching } = useQuery(['comments'], fetchComments)

    if(isLoading || isFetching) {
        return <h1>Carregando</h1>
    }

    return (
        <View>
            {
                comments.map(comment => <h3>{`${comment.id} - ${comment.userName}`}</h3>)
            }
        </View>
    )
}