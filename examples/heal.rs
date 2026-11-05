// stone:job stone:health.heal
// stone:function heal_rs

#[no_mangle]
pub extern "C" fn heal_rs(health: i32, amount: i32, max_health: i32) -> i32 {
    let health = health + amount;
    if health > max_health {
        return max_health;
    }
    health
}
