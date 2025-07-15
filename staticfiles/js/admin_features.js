document.addEventListener('DOMContentLoaded', function() {
    const featureFields = document.querySelectorAll('input[name="features"]');
    featureFields.forEach(field => {
        if (field.value) {
            const lines = field.value.split('\n').filter(line => line.trim());
            field.value = lines.join('\n');
        }

        const container = field.parentElement;
        const addButton = document.createElement('button');
        addButton.textContent = '+ Add Feature';
        addButton.type = 'button';
        addButton.style.marginTop = '5px';
        addButton.addEventListener('click', function() {
            const newInput = document.createElement('input');
            newInput.type = 'text';
            newInput.name = 'features';
            newInput.style.width = '100%';
            newInput.style.marginTop = '5px';
            container.appendChild(newInput);
        });
        container.appendChild(addButton);

        // On form submit, combine all inputs into array format
        const form = container.closest('form');
        form.addEventListener('submit', function(e) {
            const allInputs = container.querySelectorAll('input[name="features"]');
            const values = Array.from(allInputs).map(input => input.value.trim()).filter(v => v);
            field.value = JSON.stringify(values); // Convert to array string for ArrayField
        });
    });
});