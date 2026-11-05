// stone:job stone:math.avg
// stone:function avg_rs

#[no_mangle]
pub extern "C" fn avg_rs(x: f64, y: f64) -> f64 {
    (x + y) * 0.5
}
