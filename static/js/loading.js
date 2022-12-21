/**
 * @copyright T.Mallet 
 * @file loading.js
 */

/**
 * @brief Fetch loaded route then update current body html with loaded response
 */
function load() {
	fetch("loading").then(async (template) => {document.body.innerHTML = await template.text();})
}

load();
