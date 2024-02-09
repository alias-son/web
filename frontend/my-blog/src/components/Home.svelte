<script>
import { onMount } from 'svelte';
import { Link } from 'svelte-spa-router';

    let posts = [];
    let searchQuery = '';

    onMount(async () => {
        const res = await fetch('https://your-backend-api/posts');
        posts = await res.json();
    });

    $: filteredPosts = posts.filter(post => 
        post.title.toLowerCase().includes(searchQuery.toLowerCase()));
</script>

<input type="text" bind:value={searchQuery} placeholder="Search posts...">
{#each filteredPosts as post}
    <div>
        <Link to={`/post/${post.id}`}>{post.title}</Link>
    </div>
{/each}
