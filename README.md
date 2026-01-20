-Deskripsi Proyek-

Proyek ini merupakan implementasi sederhana algoritma Raft Consensus sebagai bagian dari praktikum/UAS mata kuliah Distributed Computing.

Raft adalah algoritma konsensus yang digunakan untuk menjaga konsistensi data pada sistem terdistribusi dengan cara memilih leader dan memastikan semua node mengikuti keputusan leader tersebut.

Implementasi ini berfokus pada:
- Leader Election
- Heartbeat (AppendEntries)
- RequestVote mechanism
- Simulasi fault tolerance sederhana
- Proyek dibuat untuk tujuan pembelajaran, bukan untuk produksi.

-Tujuan-
- Memahami cara kerja algoritma Raft
- Mengimplementasikan konsep konsensus terdistribusi menggunakan Python
- Mensimulasikan komunikasi antar node menggunakan socket
- Memenuhi deliverables proyek praktikum Distributed Computing

-Arsitektur Sistem-

Setiap node dijalankan sebagai proses terpisah dan saling berkomunikasi menggunakan socket TCP.
Komponen utama:
Node: Follower, Candidate, Leader
Message: RequestVote dan AppendEntries
Network: Pengiriman pesan antar node
Config: Konfigurasi node dan parameter waktu

-Struktur-
raft-consensus/
├── node.py # Logika utama Raft Node
├── message.py # Definisi message (RequestVote, AppendEntries)
├── network.py # Fungsi komunikasi socket
├── config.py # Konfigurasi node & timeout
├── README.md # Dokumentasi proyek

-Cara Menjalankan_
1️.Clone Repository
    git clone <link-repository-github>
    cd raft-consensus
2.Jalankan Node (3 Terminal Terpisah)
    Terminal 1
        python node.py 1
    Terminal 2
        python node.py 2
    Terminal 3
        python node.py 3

-Contoh Output-
[Node 1] Election term 1
[Node 1] LEADER
[Node 2] Voted for 1
[Node 2] Following leader 1
[Node 3] Following leader 1

-Referensi-
- Diego Ongaro & John Ousterhout, In Search of an Understandable Consensus Algorithm (Raft)
- https://raft.github.io/
- Distributed Systems Concepts (Lecture Materials)


-Author-

- Nama: Dicka Avrillio Pratama
- Mata Kuliah: Distributed Computing
- Institusi: STMIK AMIK Bandung

-Catatan-
- Proyek ini dibuat untuk tujuan akademik
- Implementasi disederhanakan agar mudah dipahami

- Tidak mencakup log replication secara penuh


