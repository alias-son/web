<script>
  let data = '';

  const fetchData = async () => {
    const response = await fetch('http://localhost:8000/api/data'); // FastAPI 서버 URL
    const result = await response.json();
    data = result.data;
  }

  fetchData();
</script>

<main>
  <h1>Data from FastAPI: {data}</h1>
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
  }
</style>
