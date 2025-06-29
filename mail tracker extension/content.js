console.log("📩 MailTracker content script loaded");

function injectPixelWhenComposeOpens(editor) {
/*const pixelHTML = '<img src="https://mailtracker-r0nm.onrender.com/track?email_id=' + Date.now() + '" style="display:none;">';*/
const pixelHTML = `<img src="https://mail-tracker-l9mq.onrender.com/track?email_id=${Date.now()}&rand=${Math.random()}" style="display:none;">`;



  if (!editor.innerHTML.includes('via.placeholder.com')) {
    editor.focus();
    editor.innerHTML += pixelHTML;
    console.log("✅ Tracking pixel injected as soon as compose opened.");
  }
}

window.addEventListener("load", () => {
  console.log("🔍 Gmail loaded. Starting MutationObserver...");

  const observer = new MutationObserver(() => {
    const editors = document.querySelectorAll('[role="textbox"][contenteditable="true"]');

    editors.forEach((editor) => {
      if (!editor.dataset.pixelInjected) {
        editor.dataset.pixelInjected = "true";

        injectPixelWhenComposeOpens(editor);
      }
    });
  });

  observer.observe(document.body, { childList: true, subtree: true });
});
