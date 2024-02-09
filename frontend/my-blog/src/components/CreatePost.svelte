<script>
    let title = '';
    let content = '';

    async function createPost() {
        const post = { title, content };
        await fetch('https://your-backend-api/posts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(post)
        });
        // 포스트 생성 후 홈으로 리다이렉트
    }
</script>

<form on:submit|preventDefault={createPost}>
    <input type="text" bind:value={title} placeholder="Title">
    <textarea bind:value={content} placeholder="Content"></textarea>
    <button type="submit">Create Post</button>
</form>
