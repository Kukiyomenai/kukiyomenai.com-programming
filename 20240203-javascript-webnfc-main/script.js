// script.js
const writeButton = document.getElementById('writeButton');
writeButton.addEventListener('click', async () => {
    const cardCheck = document.getElementById('cardCheck');
    const url = document.getElementById('urlWriteID').value;
    try {
        const ndef = new NDEFReader();
        await ndef.scan();
        await ndef.write({
            records: [{ recordType: "url", data: url }]
        });
        cardCheck.textContent = 'カードの状態：書き込み完了';
    } catch (e) {
        cardCheck.textContent = 'カードの状態：エラー';
    }
});

readButton.addEventListener('click', async () => {
    const cardCheck = document.getElementById('cardCheck');
    const cardStatus = document.getElementById('cardStatus');
    const ndef = new NDEFReader();
    let readingEvent = null;
    try {
        await ndef.scan();
        readingEvent = async (event) => {
            try {
                const records = event.message.records;
                if (records.length > 0 && records[0].recordType === 'url') {
                    const url = new TextDecoder().decode(records[0].data);
                    cardCheck.textContent = 'カードの状態：読み取り完了';
                    cardStatus.textContent = `カード内の情報：${url}`;
                }
            } catch (error) {
                cardCheck.textContent = 'カード内の情報：エラー';
            }

            if (readingEvent) {
                ndef.removeEventListener('reading', readingEvent);
                readingEvent = null;
            }
        };
        ndef.addEventListener('reading', readingEvent);
    } catch (error) {
        cardCheck.textContent = 'カードの状態：エラー';
    }
});
