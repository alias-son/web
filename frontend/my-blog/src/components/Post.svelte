<script>
import { onMount } from 'svelte';
import { useParams } from 'svelte-spa-router';

let post = {};
let comments = [];
const { id } = useParams();

onMount(async () => {
    const postRes = await fetch(`https://your-backend-api/posts/${id}`);
    post = await postRes.json();

    const commentsRes = await fetch(`https://your-backend-api/posts/${id}/comments`);
    comments = await commentsRes.json();
});


let newComment = "";

async function submitComment() {
    const res = await fetch(`https://your-backend-api/posts/${id}/comments`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ body: newComment, author: 'Anonymous' }) // 예시로, 사용자 이름을 'Anonymous'로 설정
    });
    if (res.ok) {
        newComment = ""; // 폼 초기화
        // 댓글 리스트를 다시 불러오거나, 댓글 배열에 직접 추가하여 UI를 업데이트할 수 있습니다.
        const addedComment = await res.json();
        comments.push(addedComment);
    }
}
</script>
    
    <div>
        <h1>{post.title}</h1>
        <p>{post.content}</p>
        <h2>Comments</h2>
        {#each comments as comment}
            <div class="comment">
                <p>{comment.author}: {comment.body}</p>
            </div>
        {/each}

        <form on:submit|preventDefault={submitComment}>
            <textarea bind:value={newComment} placeholder="Leave a comment..." rows="4"></textarea>
            <button type="submit">Submit</button>
        </form>
    </div>
    
    <style>
        .comment {
            margin-top: 10px;
            padding: 5px;
            border-bottom: 1px solid #ccc;
        }
    </style>
    