async function askAssistant() {
    const email = document.getElementById("emailInput").value;
    const responseBox = document.getElementById("responseBox");

    if (!email) {
        responseBox.innerText = "Bitte geben Sie eine E-Mail-Addresse ein.";
        return;
    }

    responseBox.innerHTML = '<span class="loading">In Verbindung mit KI... Bitte warten...</span>';

    try {
        const response = await fetch(`/ask-ai/${email}`);
        const data = await response.json();

        if (data.error) {
            responseBox.innerText = data.error
        } else {
            responseBox.innerText = data.assistant_response;
        }
    } catch (error) {
        responseBox.innerText = "Fehler bei der Verbindung zum Server.";
    }
}

async function registerCustomer() {
    const name = document.getElementById("regName").value;
    const email = document.getElementById("regEmail").value;
    const responseBox = document.getElementById("regResponseBox");

    if (!name || !email) {
        responseBox.innerText = "Bitte füllen Sie alle Felder aus."
        return;
    }

    responseBox.innerText = "Wird geladen..."

    try {
        const response = await fetch("/add-customer", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({name: name, email: email})
        });

        const data = await response.json();

        if (data.error) {
            responseBox.innerText = data.error;
            responseBox.style.color = "ef4444";
        } else {
            responseBox.innerText = data.success;
            responseBox.style.color = "10b981";
            document.getElementById("regName").value = "";
            document.getElementById("regEmail").value = "";
        }
    } catch (error) {
        responseBox.innerText = "Fehler bei der Verbindung zum Server.";
    }
}