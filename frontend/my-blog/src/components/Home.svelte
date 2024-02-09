<script>
import { onMount } from 'svelte';
import { Link } from 'svelte-spa-router';

    let posts = [];
    let searchQuery = '';

    onMount(async () => {
        const res = await fetch('http://127.0.0.1:8000/');
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
