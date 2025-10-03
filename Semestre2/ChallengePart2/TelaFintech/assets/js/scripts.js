// Banco fictício de receitas para exemplo
const recipesDB = [
  {
    id: 1,
    nome: "Maminha na Mostarda com Batatonese",
    proteina: "carne",
    carbo: 40,
    proteinaG: 50,
    gordura: 20,
    calorias: 290,
    porcoes: 5,
    preco: 68.90,
    imgThumb: "assets/images/maminha1.png",    // imagem da receita
    imgMore: "assets/images/maminha2.png",      // imagem para ingredientes e passo a passo da receita
    imgInfo: "assets/images/tabelanutricional.png",      // imagem para informacao nutricional
  },
  {
    id: 2,
    nome: "Peito de Frango com Vegetais na Grelha",
    carbo: 0,
    proteina: "frango",
    proteinaG: 55,
    gordura: 10,
    calorias: 300,
    porcoes: 4,
    preco: 35.50,
    imgThumb: "assets/images/frango1.png",
    imgMore: "assets/images/frango2.png",
    imgInfo: "assets/images/tabelanutricional.png"
  },
  {
    id: 3,
    nome: "Filé de Salmão com Crostas de Ervas Finas",
    proteina: "peixe", 
    carbo: 30, 
    proteinaG: 55, 
    gordura: 25, 
    calorias: 450, 
    porcoes: 5, 
    preco: 78.90,
    imgThumb: "assets/images/salmao1.png",
    imgMore: "assets/images/salmao2.png",
    imgInfo: "assets/images/tabelanutricional.png"
  },
  { 
    id: 4, 
    nome: "Costela Sunína com BBQ com Aligot de Mandioquinha", 
    proteina: "suino", 
    carbo: 35, 
    proteinaG: 40, 
    gordura: 30, 
    calorias: 500, 
    porcoes: 4, 
    preco: 48.90,
    imgThumb: "assets/images/costelasuina1.png",
    imgMore: "assets/images/costelasuina2.png",
    imgInfo: "assets/images/tabelanutricional.png"
  },
  { 
    id: 5, 
    nome: "Arroz de Legumes", 
    proteina: "vegetariano", 
    carbo: 50, 
    proteinaG: 35, 
    gordura: 15, 
    calorias: 380, 
    porcoes: 3,
    preco: 28.90,
    imgThumb: "assets/images/arroz1.png",
    imgMore: "assets/images/arroz2.png",
    imgInfo: "assets/images/tabelanutricional.png"
  },
];

// Estado
let goal = {};
let current = { carbo: 0, proteinaG: 0, gordura: 0, calorias: 0 };
let selections = {};

// Elementos
const buscarBtn = document.getElementById("buscarBtn");
const recipesList = document.getElementById("recipesList");
const goalDisplay = document.getElementById("goalDisplay");
const currentDisplay = document.getElementById("currentDisplay");
const goCart = document.getElementById("goCart");

const caloriasInput = document.getElementById("calorias");
const carboInput = document.getElementById("carbo");
const protInput = document.getElementById("proteina");
const gordInput = document.getElementById("gordura");

// Regras exclusivas: calorias X macros
function toggleMacroFields() {
  if (caloriasInput.value) {
    carboInput.disabled = protInput.disabled = gordInput.disabled = true;
  } else {
    carboInput.disabled = protInput.disabled = gordInput.disabled = false;
  }
}
function toggleCaloriesField() {
  if (carboInput.value || protInput.value || gordInput.value) {
    caloriasInput.disabled = true;
  } else {
    caloriasInput.disabled = false;
  }
}
[caloriasInput].forEach(inp => inp.addEventListener("input", toggleMacroFields));
[carboInput, protInput, gordInput].forEach(inp => inp.addEventListener("input", toggleCaloriesField));

// Buscar receitas
buscarBtn.addEventListener("click", () => {
  goal = {
    calorias: parseInt(caloriasInput.value) || 0,
    carbo: parseInt(carboInput.value) || 0,
    proteinaG: parseInt(protInput.value) || 0,
    gordura: parseInt(gordInput.value) || 0,
    dias: parseInt(document.getElementById("dias").value) || 7,
    refeicoes: parseInt(document.getElementById("refeicoes").value) || 3,
    proteinaTipo: document.getElementById("proteinaTipo").value
  };

  // Reset
  current = { carbo: 0, proteinaG: 0, gordura: 0, calorias: 0 };
  selections = {};
  updateSummary();
  goCart.disabled = true;

  // Filtra receitas
  let filtered = recipesDB;
  if (goal.proteinaTipo !== "todos") {
    filtered = recipesDB.filter(r => r.proteina === goal.proteinaTipo);
  }

  renderRecipes(filtered);
});

// Render receitas
function renderRecipes(recipes) {
  recipesList.innerHTML = "";
  recipes.forEach(r => {
    selections[r.id] = 0;
    const card = document.createElement("div");
    card.className = "d-flex justify-content-between align-items-center border rounded p-2 mb-2 bg-white";
    card.innerHTML = `
      <div class="d-flex align-items-center p-2">
        <img src="${r.imgThumb}" alt="${r.nome}" style="width:150px; height:150px; object-fit:cover; border-radius:8px; margin-right:10px;">
        <div class="text-start">
          <h6 class="mb-1">${r.nome} <small class="text-muted">(Rende ${r.porcoes} porções)</small></h6>
          <p class="mb-0">${r.carbo}g Carbo | ${r.proteinaG}g Prot | ${r.gordura}g Gord | ${r.calorias} kcal</p>
          <small class="text-muted">Preço: R$ ${r.preco.toFixed(2)}</small>
        </div>
      </div>
      <div class="d-flex align-items-center p-2">
        <button class="btn btn-sm me-1" onclick="openModal('${r.imgMore}')">
          <img src="assets/images/view.png" alt="Ícone" class="eye" style="width: 28px; height: 28px;">
        </button>
        <button class="btn btn-sm me-3" onclick="openModal('${r.imgInfo}')">
          <img src="assets/images/info1.png" alt="Ícone" class="info" style="width: 28px; height: 28px;">
        </button>
        <button class="btn btn-sm btn-warning me-1" onclick="updateMeal(${r.id}, -1)">–</button>
        <span id="qty-${r.id}" class="fw-bold">0</span>
        <button class="btn btn-sm btn-warning ms-1" onclick="updateMeal(${r.id}, 1)">+</button>
      </div>
    `;
    recipesList.appendChild(card);
  });
}

// Função para abrir modal com imagem
function openModal(imgSrc) {
  const modal = document.getElementById("imgModal");
  const modalImg = document.getElementById("modalImg");
  modal.style.display = "flex";
  modalImg.src = imgSrc;
}

// Fechar modal
function closeModal() {
  document.getElementById("imgModal").style.display = "none";
}

// Atualiza seleção
function updateMeal(id, delta) {
  const meal = recipesDB.find(r => r.id === id);
  selections[id] = Math.max(0, selections[id] + delta);

  document.getElementById(`qty-${id}`).textContent = selections[id];

  // Zera e recalcula
  current = { carbo: 0, proteinaG: 0, gordura: 0, calorias: 0 };
  Object.keys(selections).forEach(key => {
    const qtd = selections[key];
    if (qtd > 0) {
      const m = recipesDB.find(r => r.id == key);
      current.carbo += m.carbo * qtd;
      current.proteinaG += m.proteinaG * qtd;
      current.gordura += m.gordura * qtd;
      current.calorias += m.calorias * qtd;
    }
  });

  updateSummary();
  goCart.disabled = Object.values(selections).every(q => q === 0);
}

// Atualiza resumo
function updateSummary() {
  const totalMeals = Object.values(selections).reduce((a, b) => a + b, 0);
  const daysComplete = Math.floor(totalMeals / goal.refeicoes);
  const remainingMeals = goal.dias * goal.refeicoes - totalMeals;

  // médias por dia
  const avgCalories = daysComplete > 0 ? Math.round(current.calorias / daysComplete) : 0;
  const avgCarbo = daysComplete > 0 ? Math.round(current.carbo / daysComplete) : 0;
  const avgProt = daysComplete > 0 ? Math.round(current.proteinaG / daysComplete) : 0;
  const avgGord = daysComplete > 0 ? Math.round(current.gordura / daysComplete) : 0;

  goalDisplay.textContent = 
    `Objetivo: Calorias/dia: ${goal.calorias || "-"} | Carbo: ${goal.carbo} g | Prot: ${goal.proteinaG} g | Gord: ${goal.gordura} g | Dias: ${goal.dias} | Refeições/dia: ${goal.refeicoes}`;
  
  currentDisplay.innerHTML = 
    `Selecionado: Calorias/dia: ${avgCalories} | Carbo: ${avgCarbo} g | Prot: ${avgProt} g | Gord: ${avgGord} g | Dias completos: ${daysComplete} | Refeições: ${totalMeals} <br>
    <small class="text-muted">(${remainingMeals > 0 ? remainingMeals + " refeições faltando para atingir " + goal.dias + " dias" : "Meta atingida"})</small>`;
}

// Botão Carrinho (só leva pro topo)
goCart.addEventListener("click", () => {
  window.scrollTo({ top: 0, behavior: "smooth" });
});
