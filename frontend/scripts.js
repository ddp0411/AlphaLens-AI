async function getRecommendation() {
  const symbol = document.getElementById("symbol").value;
  const res = await fetch(`http://localhost:8000/recommendation/run?symbol=${symbol}`);
  const data = await res.json();
  document.getElementById("result").textContent = JSON.stringify(data, null, 2);
}
