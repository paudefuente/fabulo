import express, { Request, Response } from 'express';
import { PythonShell } from 'python-shell';
import path from 'path';

const app = express();
const port = 3000;

app.use(express.json());

app.post('/encrypt', (req: Request, res: Response) => {
    const { session_key, data, iv } = req.body;

    let options = {
        mode: 'json',
        pythonOptions: ['-u'],
        scriptPath: path.join(__dirname, 'scripts', 'encryption'),
        args: [JSON.stringify({ session_key, data, iv })]
    };

    PythonShell.run('main.py', options, function (err, results) {
        if (err) {
            console.error(err);
            return res.status(500).send(`Server Error: ${err.message}`);
        }

        if (results && results.length > 0) {
            res.json(results[0]);
        } else {
            res.status(500).send('No result returned from Python script');
        }
    });
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});