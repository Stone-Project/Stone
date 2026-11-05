// stone:job stone:math.noise1
// stone:function noise1_rs

#[no_mangle]
pub extern "C" fn noise1_rs(x: f64) -> f64 {
    let i = x.floor();
    let f = x - i;
    let ii = i as i64;
    let a = ((((ii as i128) * 1103515245 + 12345) as i64) & 0x7FFFFFFF) as f64 / 0x7FFFFFFF as f64;
    let b = (((((ii + 1) as i128) * 1103515245 + 12345) as i64) & 0x7FFFFFFF) as f64 / 0x7FFFFFFF as f64;
    let u = f * f * (3.0 - 2.0 * f);
    a + (b - a) * u
}
