use tokio::time::Duration;

#[tokio::main]
async fn main() {
    println!("ARGUS P2P Node starting...");
    loop {
        tokio::time::sleep(Duration::from_secs(60)).await;
        println!("Node running...");
    }
}
