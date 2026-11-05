// stone:job stone:math.add
// stone:function add_rs

#[no_mangle]
pub extern "C" fn add_rs(x: f64, y: f64) -> f64 {
    x + y
}
